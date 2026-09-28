import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Extract text from a small page range of a PDF inside Papers/. Use this instead of reading an entire scientific PDF. Maximum 4 pages per call.",
  args: {
    path: tool.schema.string().describe("Vault-relative PDF path inside Papers/, for example Papers/article.pdf"),
    start_page: tool.schema.number().int().min(1).describe("First 1-based PDF page to extract"),
    end_page: tool.schema.number().int().min(1).describe("Last 1-based PDF page to extract; at most 4 pages per call"),
    max_chars: tool.schema.number().int().min(4000).max(40000).optional().describe("Maximum returned characters; default 24000")
  },
  async execute(args, context) {
    if (args.end_page < args.start_page) return "ERROR: end_page must be >= start_page"
    if (args.end_page - args.start_page + 1 > 4) return "ERROR: request at most 4 pages per call"
    const script = path.join(context.worktree, ".opencode", "tools", "pdf_pages.py")
    const maxChars = args.max_chars ?? 24000
    const commonArgs = [script, args.path, String(args.start_page), String(args.end_page), String(maxChars)]
    const candidates: string[][] = process.platform === "win32"
      ? [["python", ...commonArgs], ["py", "-3", ...commonArgs]]
      : [["python3", ...commonArgs], ["python", ...commonArgs]]
    let lastError = ""
    for (const command of candidates) {
      try {
        const proc = Bun.spawn(command, { cwd: context.worktree, stdout: "pipe", stderr: "pipe" })
        const stdout = await new Response(proc.stdout).text()
        const stderr = await new Response(proc.stderr).text()
        const code = await proc.exited
        if (code === 0) return stdout.trim()
        lastError = `${command[0]} exited with code ${code}: ${stderr || stdout}`
      } catch (err) {
        lastError = `${command[0]} failed: ${String(err)}`
      }
    }
    return `ERROR: could not extract PDF pages. ${lastError}`
  }
})

# Claude Skills Playground

A collection of custom skills for Claude Code that extend Claude's capabilities with specialized workflows and tools.

## What Are Claude Skills?

Claude skills are packages that provide Claude with specialized knowledge and workflows for specific tasks. Each skill contains instructions, scripts, and assets that enable Claude to perform complex multi-step operations autonomously.

## Available Skills

### 🍕 Family Menu Generator (`family-menu`)
Creates beautiful, protein-focused weekly dinner menus for families with research capabilities.

**Key Features:**
- Protein-focused meal planning
- Leftover detection and planning
- Local restaurant recommendations
- Seasonal ingredient research
- Random beautiful PDF designs (5 styles)
- Homemade Pizza Fridays
- Print-ready 8.5x11 PDFs

**Use when:** Planning weekly family dinners, creating refrigerator menus, or meal planning assistance.

### 💡 Brainstorming (`brainstorm-it`)
Refines rough ideas into fully-formed designs through structured Socratic questioning and alternative exploration.

**Key Features:**
- Structured 4-phase ideation process
- Current state assessment
- Alternative approach exploration
- Incremental design validation
- Git worktree workflow integration
- Implementation planning

**Use when:** Creating or developing anything before writing code or implementation plans - transforms ideas into actionable designs.

### 📄 Resume Builder (`resume-builder`)
Generate beautiful, professionally designed resumes as 1-2 page PDFs.

**Key Features:**
- Clean, sophisticated layouts
- Job-specific tailoring
- Address verification workflow
- Optional cover letter generation
- Custom typography from included fonts
- ATS-friendly formatting

**Use when:** Creating professional resumes, tailoring applications to specific job postings, or generating matching cover letters.

## Installation

To use these skills with Claude Code:

1. **Navigate to the skill directory** you want to install (e.g., `family-menu/`, `brainstorm-it/`, or `resume-builder/`)

2. **Create a zip file** of the entire directory contents:
   ```bash
   # From the repository root
   cd family-menu
   zip -r ../family-menu.zip .
   cd ..
   ```

   Or for all skills:
   ```bash
   # Create zip files for each skill
   cd family-menu && zip -r ../family-menu.zip . && cd ..
   cd brainstorm-it && zip -r ../brainstorm-it.zip . && cd ..
   cd resume-builder && zip -r ../resume-builder.zip . && cd ..
   ```

3. **Upload to Claude Code:**
   - Open Claude Code
   - Navigate to the Skills section
   - Click "Add Skill" or "Upload Skill"
   - Select the `.zip` file you created
   - Claude will automatically extract and load the skill

## Skill Structure

Each skill directory follows this structure:

```
skill-name/
├── SKILL.md              # Main instructions for Claude
├── scripts/              # Python/bash scripts (if needed)
├── assets/               # Fonts, images, templates (if needed)
├── references/           # Documentation, examples (if needed)
└── LICENSE.txt           # License information (if applicable)
```

The `SKILL.md` file contains:
- **Frontmatter**: Name, description, and metadata
- **Instructions**: Detailed workflow and guidelines for Claude
- **Resources**: Information about included scripts and assets

## Usage

Once installed, skills are automatically available to Claude. Claude will recognize when to use each skill based on:

- The skill's description in the frontmatter
- Context clues in your conversation
- Explicit requests (e.g., "Use the brainstorming skill to help me design this feature")

## Development

### Creating New Skills

1. Create a new directory with your skill name
2. Add a `SKILL.md` file with frontmatter and instructions
3. Include any necessary scripts in a `scripts/` directory
4. Add assets (fonts, templates, etc.) to an `assets/` directory
5. Test the skill with Claude
6. Zip the directory for distribution

### Modifying Existing Skills

1. Edit the appropriate `SKILL.md` or script files
2. Re-zip the skill directory
3. Re-upload to Claude Code (may need to remove old version first)

## Requirements

Skills may have different dependencies:

- **Family Menu Generator**: Requires Python with `reportlab` library
- **Brainstorm-it**: No external dependencies
- **Resume Builder**: Requires Python with PDF generation libraries (e.g., `reportlab`)

Check each skill's `SKILL.md` for specific requirements.

## Contributing

Feel free to:
- Report issues or suggest improvements
- Create new skills following the existing patterns
- Share your modified versions
- Submit pull requests with enhancements

## License

Each skill may have its own license. Check the individual skill directories for license information.

---

**Note:** These skills are designed for Claude Code and require the Claude interface to function. The zip files should contain all directory contents including the `SKILL.md` file, scripts, and assets.

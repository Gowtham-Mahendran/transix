## Publishing Checklist

Before publishing your package to PyPI, verify:

- [ ] All tests pass across Python versions  
- [ ] Code is formatted and linted `uv run ruff check .`
- [ ] `README.md` is complete with examples  
- [ ] `LICENSE` file is included  
- [ ] Version number is updated  
- [ ] `CHANGELOG.md` is updated  
- [ ] Dependencies are correctly specified  
- [ ] Package builds without errors (`uv build`)  
- [ ] Package tested on **TestPyPI**  
- [ ] Documentation is up to date  
- [ ] Git repository is tagged with version  
- [ ] GitHub release is created (for trusted publishing)  

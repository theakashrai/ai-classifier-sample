# Contributing to AI Classifier Sample

Thank you for your interest in contributing to AI Classifier Sample! This document provides guidelines and information for contributors.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- Poetry for dependency management
- Git for version control

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/your-username/ai-classifier-sample.git
cd ai-classifier-sample
```

3. Install dependencies:

```bash
poetry install --with dev
```

4. Install pre-commit hooks:

```bash
poetry run pre-commit install
```

## Development Workflow

### Making Changes

1. Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bugfix-name
```

2. Make your changes following the code standards below
3. Add or update tests as necessary
4. Update documentation if needed

### Code Standards

- **Style**: Use `black` for code formatting
- **Imports**: Use `isort` for import sorting  
- **Linting**: Follow `flake8` guidelines
- **Type Hints**: Include type hints for all function signatures
- **Docstrings**: Document public APIs with clear docstrings
- **Tests**: Write tests for new features and bug fixes

### Running Quality Checks

Before committing, run the following checks:

```bash
# Format code
poetry run black .
poetry run isort .

# Remove unused imports
poetry run autoflake --remove-all-unused-imports --recursive --in-place .

# Run linting
poetry run flake8 .

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=ai_classifier_sample
```

### Commit Guidelines

- Use clear, descriptive commit messages
- Follow the format: `type: description`
- Examples:
  - `feat: add support for new AI provider`
  - `fix: handle edge case in message classification`
  - `docs: update installation instructions`
  - `test: add unit tests for settings module`

## Testing

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest tests/test_settings.py

# Run tests with coverage report
poetry run pytest --cov=ai_classifier_sample --cov-report=html

# Run specific test categories
poetry run pytest -m unit
poetry run pytest -m integration
```

### Writing Tests

- Place tests in the `tests/` directory
- Follow the naming convention: `test_*.py`
- Use descriptive test names that explain what is being tested
- Include both positive and negative test cases
- Mock external dependencies appropriately

## Adding New Features

### AI Provider Support

To add support for a new AI provider:

1. Create a new provider module in `src/ai_classifier_sample/providers/`
2. Implement the required interface methods
3. Update configuration settings to include the new provider
4. Add comprehensive tests for the new provider
5. Update documentation with usage examples

### Configuration Options

When adding new configuration options:

1. Add the option to the settings model in `src/ai_classifier_sample/config/settings.py`
2. Include appropriate validation and default values
3. Update the README with the new environment variable
4. Add tests to verify the configuration works correctly

## Pull Request Process

1. Ensure all tests pass and code quality checks are clean
2. Update the CHANGELOG.md with your changes
3. Update documentation if necessary
4. Submit a pull request with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference any related issues
   - Screenshots or examples if applicable

### Pull Request Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

## Release Process

Releases are handled by maintainers and follow semantic versioning:

- **Major** (x.0.0): Breaking changes
- **Minor** (0.x.0): New features, backwards compatible
- **Patch** (0.0.x): Bug fixes, backwards compatible

## Getting Help

If you need help or have questions:

1. Check existing issues on GitHub
2. Review the documentation in the README
3. Create a new issue with the `question` label
4. Reach out to maintainers for complex topics

Thank you for contributing to AI Classifier Sample! 🎉

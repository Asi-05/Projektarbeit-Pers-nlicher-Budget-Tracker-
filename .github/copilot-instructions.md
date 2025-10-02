# Personal Budget Tracker - AI Coding Instructions

This is a **German-language personal budget tracker** console application for a FHNW Programming Foundations student project. The actual implementation differs from the template README.md which describes a pizza ordering system.

## 🏗️ Architecture Overview

**Current State**: Early development - basic menu structure exists but core functionality needs implementation.

- **`main.py`**: Main program logic with German console interface for budget tracking
- **`menü.py`**: Placeholder file for menu functionality (currently minimal)
- **Language**: All user-facing text is in German
- **Pattern**: Console-based application with menu-driven interaction

## 🔧 Key Implementation Patterns

### German Language UI
The application uses German text throughout:
```python
print("=== Willkommen zu deinem Budgetplaner ===")
print("1) Einnahmen hinzufügen")  # Add income
print("2) Ausgaben hinzufügen")   # Add expenses
print("3) Übersicht anzeigen")    # Show overview
```

### Menu Structure
Following the established pattern in `main.py`:
- Function-based menu system with `start_menu()`
- Numeric choice input validation needed
- Main loop with option handling
- Clear German prompts and error messages

### Critical Bug to Fix
**IMPORTANT**: `main.py` line 11 has a bug - missing function call parentheses:
```python
# Current (broken):
auswahl = start_menu

# Should be:
auswahl = start_menu()
```

## 📋 Project Requirements (Per README Template)

Must implement these three core features:
1. **Interactive console input** - Menu-driven interface ✅ (started)
2. **Data validation** - Input checking for all user entries ❌ (not implemented)
3. **File processing** - Read/write budget data ❌ (not implemented)

## 🎯 Expected Features to Implement

Based on the German menu options:
- **Einnahmen hinzufügen**: Add income entries with validation
- **Ausgaben hinzufügen**: Add expense entries with validation  
- **Übersicht anzeigen**: Display budget overview/summary
- **Edit**: Modify existing entries

### File Structure Recommendations
```
├── main.py              # Main program (current)
├── menü.py             # Menu functionality (expand this)
├── budget_data.txt     # Store budget entries
├── README.md           # Update to match actual project
```

## 🛠️ Development Workflow

**Setup**: Standard Python 3.x, no external dependencies
**Testing**: Run with `python3 main.py`
**Language**: Maintain German interface consistently

## 🚨 Critical Notes

- **README Mismatch**: Current README.md describes a pizza system but code implements budget tracker
- **Early Stage**: Core functionality not yet implemented
- **Student Project**: This is educational code for FHNW Programming Foundations
- **File Processing**: Will need to implement reading/writing budget data to meet project requirements

## 💡 AI Assistance Guidelines

When helping with this codebase:
1. **Always use German** for user-facing text and comments
2. **Fix the function call bug** in main.py before other changes
3. **Implement data validation** for numeric inputs (income/expense amounts)
4. **Add file processing** for persistent budget storage
5. **Keep it simple** - this is a beginner Python project
6. **Follow the menu pattern** established in main.py for consistency
import re
import tkinter as tk
from tkinter import ttk, messagebox

def check_password_strength(password):
    score = 0
    feedback = []  # Corrected - initialized as a list

    if len(password) >= 8:
        score += 20
        feedback.append("✅ Good length.")
    else:
        feedback.append("❌ Too short. Use at least 8 characters.")

    if re.search("[A-Z]", password):
        score += 20
        feedback.append("✅ Contains uppercase letters.")
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search("[a-z]", password):
        score += 20
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search("[0-9]", password):  # Corrected regex for numbers
        score += 20
        feedback.append("✅ Contains numbers.")
    else:
        feedback.append("❌ Add at least one number.")

    if re.search("[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):  # Special characters
        score += 20
        feedback.append("✅ Contains special characters.")
    else:
        feedback.append("❌ Add at least one special character.")

    # Strength classification
    if score < 40:
        strength = "Weak"
    elif score < 60:
        strength = "Moderate"
    elif score < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {"score": score, "feedback": feedback, "strength": strength}  # Fixed return statement


def analyze_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    result = check_password_strength(password)

    strength_label.config(text=f"Strength: {result['strength']}")
    score_label.config(text=f"Score: {result['score']}/100")
    
    feedback_text.config(state=tk.NORMAL)  # Enable editing
    feedback_text.delete("1.0", tk.END)  # Clear previous feedback

    for message in result['feedback']:
        feedback_text.insert(tk.END, f"{message}\n")

    feedback_text.config(state=tk.DISABLED)  # Disable editing after updating


def clear_fields():
    password_entry.delete(0, tk.END)
    strength_label.config(text="Strength: ")
    score_label.config(text="Score: ")
    
    feedback_text.config(state=tk.NORMAL)  # Enable before clearing
    feedback_text.delete("1.0", tk.END)
    feedback_text.config(state=tk.DISABLED)  # Disable again


# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")  # Set a default size

# Styling
style = ttk.Style()
style.theme_use("clam")  # Optional for better visuals

# Labels and Entries
password_label = ttk.Label(root, text="Enter Password:")
password_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

password_entry = ttk.Entry(root, show="*")  # Mask password input
password_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
password_entry.focus()

# Analyze Button
analyze_button = ttk.Button(root, text="Analyze", command=analyze_password)
analyze_button.grid(row=1, column=0, columnspan=2, pady=10)

# Strength and Score Display
strength_label = ttk.Label(root, text="Strength: ")
strength_label.grid(row=2, column=0, sticky="w")

score_label = ttk.Label(root, text="Score: ")
score_label.grid(row=3, column=0, sticky="w")

# Feedback Text Area
feedback_label = ttk.Label(root, text="Feedback:")
feedback_label.grid(row=4, column=0, sticky="w")

feedback_text = tk.Text(root, height=7, width=40)
feedback_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
feedback_text.config(state=tk.DISABLED)  # Make it read-only

# Clear Button
clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=6, column=0, columnspan=2, pady=10)

# Adjust Grid for Resizing
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()

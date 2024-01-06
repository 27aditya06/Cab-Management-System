import tkinter as tk
from tkinter import messagebox

class Cab:
    def __init__(self, cab_id, is_available=True):
        self.cab_id = cab_id
        self.is_available = is_available

class CabManagementSystem:
    def __init__(self):
        self.cabs = {}

    def add_cab(self, cab_id):
        if cab_id not in self.cabs:
            self.cabs[cab_id] = Cab(cab_id)
            return f"Cab {cab_id} added successfully."
        else:
            return f"Cab {cab_id} already exists."

    def display_available_cabs(self):
        available_cabs = [cab_id for cab_id, cab in self.cabs.items() if cab.is_available]
        return available_cabs

    def request_cab(self):
        available_cabs = [cab_id for cab_id, cab in self.cabs.items() if cab.is_available]
        if not available_cabs:
            return None
        else:
            cab_id = available_cabs[0]
            self.cabs[cab_id].is_available = False
            return cab_id

    def release_cab(self, cab_id):
        if cab_id in self.cabs:
            self.cabs[cab_id].is_available = True
            return f"Cab ID: {cab_id} released."
        else:
            return f"Cab ID: {cab_id} not found."

    def display_all_cabs(self):
        return list(self.cabs.keys())  # Return a list of all cab IDs

    def get_cab_details(self, cab_id):
        if cab_id in self.cabs:
            return f"Cab ID: {cab_id}, Available: {self.cabs[cab_id].is_available}"
        else:
            return f"Cab ID: {cab_id} not found."

class CabManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cab Management System")
        self.cab_system = CabManagementSystem()

        self.label = tk.Label(root, text="Welcome to Cab Management System", font=("Arial", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.add_cab_label = tk.Label(root, text="Add a Cab:", font=("Arial", 14))
        self.add_cab_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.add_cab_entry = tk.Entry(root, font=("Arial", 12))
        self.add_cab_entry.grid(row=1, column=1, pady=5)
        self.add_cab_button = tk.Button(root, text="Add Cab", command=self.add_cab, font=("Arial", 12, "bold"), bg="green", fg="white")
        self.add_cab_button.grid(row=1, column=2, padx=10, pady=5)

        self.available_cabs_label = tk.Label(root, text="Available Cabs:", font=("Arial", 14))
        self.available_cabs_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.available_cabs_text = tk.Text(root, height=5, width=30, font=("Arial", 12))
        self.available_cabs_text.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        self.request_cab_button = tk.Button(root, text="Request Cab", command=self.request_cab, font=("Arial", 12, "bold"), bg="blue", fg="white")
        self.request_cab_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.release_cab_label = tk.Label(root, text="Release a Cab:", font=("Arial", 14))
        self.release_cab_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        self.release_cab_entry = tk.Entry(root, font=("Arial", 12))
        self.release_cab_entry.grid(row=4, column=1, pady=5)
        self.release_cab_button = tk.Button(root, text="Release Cab", command=self.release_cab, font=("Arial", 12, "bold"), bg="red", fg="white")
        self.release_cab_button.grid(row=4, column=2, padx=10, pady=5)

        # New Feature: Display All Cabs Button
        self.display_all_cabs_button = tk.Button(root, text="Display All Cabs", command=self.display_all_cabs,
                                                 font=("Arial", 12, "bold"), bg="purple", fg="white")
        self.display_all_cabs_button.grid(row=5, column=0, columnspan=2, pady=5)

        # New Feature: Get Cab Details Entry and Button
        self.get_cab_details_label = tk.Label(root, text="Get Cab Details:", font=("Arial", 14))
        self.get_cab_details_label.grid(row=6, column=0, sticky='w', padx=10, pady=5)
        self.get_cab_details_entry = tk.Entry(root, font=("Arial", 12))
        self.get_cab_details_entry.grid(row=6, column=1, pady=5)
        self.get_cab_details_button = tk.Button(root, text="Get Details", command=self.get_cab_details,
                                                font=("Arial", 12, "bold"), bg="orange", fg="white")
        self.get_cab_details_button.grid(row=6, column=2, padx=10, pady=5)

        self.update_available_cabs()

    def add_cab(self):
        cab_id = self.add_cab_entry.get()
        result = self.cab_system.add_cab(cab_id)
        messagebox.showinfo("Add Cab", result)
        self.update_available_cabs()

    def update_available_cabs(self):
        available_cabs = self.cab_system.display_available_cabs()
        self.available_cabs_text.delete(1.0, tk.END)
        if available_cabs:
            for cab in available_cabs:
                self.available_cabs_text.insert(tk.END, f"{cab}\n")

    def request_cab(self):
        assigned_cab = self.cab_system.request_cab()
        if assigned_cab:
            messagebox.showinfo("Request Cab", f"Cab {assigned_cab} assigned.")
            self.update_available_cabs()
        else:
            messagebox.showinfo("Request Cab", "Sorry, no cabs available at the moment.")

    def release_cab(self):
        cab_id = self.release_cab_entry.get()
        result = self.cab_system.release_cab(cab_id)
        messagebox.showinfo("Release Cab", result)
        self.update_available_cabs()

    def display_all_cabs(self):
        all_cabs = self.cab_system.display_all_cabs()
        messagebox.showinfo("All Cabs", f"All Cabs: {', '.join(all_cabs)}")

    def get_cab_details(self):
        cab_id = self.get_cab_details_entry.get()
        details = self.cab_system.get_cab_details(cab_id)
        messagebox.showinfo("Cab Details", details)

if __name__ == "__main__":
    root = tk.Tk()
    app = CabManagementApp(root)
    root.geometry("400x600")  # Increased window height to accommodate new features
    root.mainloop()

 
import tkinter as tk
from tkinter import filedialog
import subprocess                            # It looks like you've started a Python script using the Tkinter library for creating a graphical user interface (GUI) and the subprocess and shutil modules for handling files and processes
import shutil

class HadoopGUI:
    def __init__(self, master):              # def __init__(self, master):: This is the constructor method . It takes two parameters: self (a reference to the instance of the class) and master. The master parameter is likely to be the                                            main window or the root of your Tkinter application.
    
        self.master = master                #assign 'master' to instance
        self.master.title("Hadoop GUI")     #the title of the main window to "Hadoop GUI".

        # Start and Stop Hadoop buttons
        self.start_button = tk.Button(master, text="Start Hadoop", command=self.start_hadoop)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Hadoop", command=self.stop_hadoop)
        self.stop_button.pack()

        # Load MapReduce JAR File
        self.load_jar_button = tk.Button(master, text="Load JAR File", command=self.load_jar)
        self.load_jar_button.pack()

        # Input and Output Data files
        self.input_label = tk.Label(master, text="Input Data File:")
        self.input_label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.output_label = tk.Label(master, text="Output Data File:")
        self.output_label.pack()

        self.output_entry = tk.Entry(master)
        self.output_entry.pack()

        # Copy result data into local file button
        self.copy_result_button = tk.Button(master, text="Copy Result Data", command=self.copy_result_data)
        self.copy_result_button.pack()

    def start_hadoop(self):
       try:
            # Replace '/path/to/hadoop' with the actual path to your Hadoop installation
            hadoop_start_cmd = "/usr/local/hadoop/sbin/start-all.sh"

            
            # Execute the Hadoop start command
            subprocess.run(hadoop_start_cmd, shell=True, check=True)
            
            print("Hadoop started successfully.")
       except subprocess.CalledProcessError as e:
            print(f"Error starting Hadoop: {e}")

 
    def stop_hadoop(self):
         try:
            # Replace '/path/to/hadoop' with the actual path to your Hadoop installation
            hadoop_stop_cmd = "/usr/local/hadoop/sbin/stop-all.sh"
            
            # Execute the Hadoop stop command
            subprocess.run(hadoop_stop_cmd, shell=True, check=True)
            
            print("Hadoop stopped successfully.")
         except subprocess.CalledProcessError as e:
            print(f"Error stopping Hadoop: {e}")

    def load_jar(self):
         # Open a file dialog to select a JAR file
        file_path = filedialog.askopenfilename(title="Select JAR File", filetypes=[("JAR files", "task2.jar")])     # This function opens a file dialog and returns the selected file's path. It allows the user to choose an           existing file.

        # Display the selected JAR file path in the GUI or perform any other action
        print(f"Selected JAR file: {file_path}")

    def copy_result_data(self):
        try:
            # Get input and output file paths
            input_data_path = self.input_entry.get()
            output_data_path = self.output_entry.get()

            # Copy result data from input to output
            shutil.copy(input_data_path, output_data_path)
            print(f"Result data copied from {input_data_path} to {output_data_path}")
        except Exception as e:
            print(f"Error copying result data: {e}")
if __name__ == "__main__":
    root = tk.Tk()  #: Creates the main application window.
    app = HadoopGUI(root)        #: Creates an instance of the HadoopGUI class with the root window as the master.
    root.mainloop()  # Starts the Tkinter event loop, which listens for user input and events.

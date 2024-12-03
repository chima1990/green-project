import tkinter as tk
from tkinter import ttk
import random
import time

class GreenhouseSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Greenhouse Dashboard")

        # Initialize variables
        self.temperature = 25.0
        self.humidity = 60.0
        self.light_level = 100.0
        self.soil_moisture = 50.0

        self.fan_on = False
        self.sprinkler_on = False
        self.lights_on = False
        self.heater_on = False

        self.ideal_temp = 25.0
        self.ideal_humidity = 60.0
        self.ideal_light = 75.0
        self.ideal_moisture = 50.0

        self.temp_tolerance = 2.0
        self.humidity_tolerance = 5.0
        self.light_tolerance = 10.0
        self.moisture_tolerance = 5.0

        self.create_widgets()
        self.update_environment()

    def create_widgets(self):
        # Create frames
        self.readings_frame = ttk.LabelFrame(self.master, text="Current Readings")
        self.readings_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.controls_frame = ttk.LabelFrame(self.master, text="Controls Status")
        self.controls_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.settings_frame = ttk.LabelFrame(self.master, text="Ideal Settings")
        self.settings_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Create readings display
        self.create_reading_display("Temperature", "temperature", "°C", self.readings_frame)
        self.create_reading_display("Humidity", "humidity", "%", self.readings_frame)
        self.create_reading_display("Light Level", "light_level", "lux", self.readings_frame)
        self.create_reading_display("Soil Moisture", "soil_moisture", "%", self.readings_frame)

        # Create controls display
        self.create_control_display("Fan", "fan", self.controls_frame)
        self.create_control_display("Sprinkler", "sprinkler", self.controls_frame)
        self.create_control_display("Lights", "lights", self.controls_frame)
        self.create_control_display("Heater", "heater", self.controls_frame)

        # Create settings inputs
        self.create_setting_input("Ideal Temperature", "ideal_temp", "°C", self.settings_frame)
        self.create_setting_input("Ideal Humidity", "ideal_humidity", "%", self.settings_frame)
        self.create_setting_input("Ideal Light Level", "ideal_light", "lux", self.settings_frame)
        self.create_setting_input("Ideal Soil Moisture", "ideal_moisture", "%", self.settings_frame)

    def create_reading_display(self, label_text, variable_name, unit, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = ttk.Label(frame, text=f"{label_text}:")
        label.pack(side=tk.LEFT)

        value_label = ttk.Label(frame, text="0 " + unit)
        value_label.pack(side=tk.RIGHT)

        setattr(self, f"{variable_name}_label", value_label)

    def create_control_display(self, label_text, variable_name, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = ttk.Label(frame, text=f"{label_text}:")
        label.pack(side=tk.LEFT)

        status_label = ttk.Label(frame, text="OFF")
        status_label.pack(side=tk.RIGHT)

        setattr(self, f"{variable_name}_status", status_label)

    def create_setting_input(self, label_text, variable_name, unit, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = ttk.Label(frame, text=f"{label_text}:")
        label.pack(side=tk.LEFT)

        var = tk.StringVar(value=str(getattr(self, variable_name)))
        entry = ttk.Entry(frame, textvariable=var, width=10)
        entry.pack(side=tk.RIGHT)

        unit_label = ttk.Label(frame, text=unit)
        unit_label.pack(side=tk.RIGHT)

        var.trace("w", lambda name, index, mode, var=var, attr=variable_name: self.update_setting(var, attr))

    def update_setting(self, var, attr):
        try:
            value = float(var.get())
            setattr(self, attr, value)
        except ValueError:
            pass  # Ignore invalid input

    def update_environment(self):
        self.simulate_environment()
        self.update_controls()
        self.update_display()
        self.master.after(1000, self.update_environment)

    def simulate_environment(self):
        # Simulate natural changes
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-1, 1)
        self.light_level = max(0, min(100, self.light_level + random.uniform(-5, 5)))
        self.soil_moisture += random.uniform(-0.5, 0.5)

        # Simulate day/night cycle
        current_time = time.localtime().tm_hour
        if 6 <= current_time < 18:
            self.light_level = min(100, self.light_level + 5)
        else:
            self.light_level = max(0, self.light_level - 5)

        # Apply effects of controls
        if self.fan_on:
            self.temperature -= 0.5
            self.humidity -= 1
        if self.heater_on:
            self.temperature += 0.5
        if self.sprinkler_on:
            self.humidity += 1
            self.soil_moisture += 0.5
        if self.lights_on:
            self.light_level = min(100, self.light_level + 10)

    def update_controls(self):
        # Update controls based on current conditions and ideal settings
        self.fan_on = (self.temperature > self.ideal_temp + self.temp_tolerance) or (self.humidity > self.ideal_humidity + self.humidity_tolerance)
        self.heater_on = self.temperature < self.ideal_temp - self.temp_tolerance
        self.sprinkler_on = self.soil_moisture < self.ideal_moisture - self.moisture_tolerance
        self.lights_on = self.light_level < self.ideal_light - self.light_tolerance

    def update_display(self):
        # Update readings
        self.update_reading("temperature", self.temperature, "°C")
        self.update_reading("humidity", self.humidity, "%")
        self.update_reading("light_level", self.light_level, "lux")
        self.update_reading("soil_moisture", self.soil_moisture, "%")

        # Update control status
        self.update_control_status("fan", self.fan_on)
        self.update_control_status("sprinkler", self.sprinkler_on)
        self.update_control_status("lights", self.lights_on)
        self.update_control_status("heater", self.heater_on)

    def update_reading(self, name, value, unit):
        label = getattr(self, f"{name}_label")
        label.config(text=f"{value:.1f} {unit}")

    def update_control_status(self, name, is_on):
        label = getattr(self, f"{name}_status")
        label.config(text="ON" if is_on else "OFF")

root = tk.Tk()
app = GreenhouseSimulator(root)
root.mainloop()
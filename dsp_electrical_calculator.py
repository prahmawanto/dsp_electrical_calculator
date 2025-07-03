import math

class ElectricalCalculator:
    def __init__(self):
        self.pi = math.pi
        self.sqrt3 = math.sqrt(3)
        
    def show_formula(self, formula_name):
        """Displays formulas during program execution"""
        formulas = {
            'ac_voltage': [
                "AC Voltage Formulas:",
                "Vrms = Vpeak/√2",
                "Vpeak = Vrms×√2"
            ],
            'single_phase': [
                "Single-Phase Power Formulas:",
                "P = Vrms × Irms × cosθ",
                "Q = Vrms × Irms × sinθ",
                "S = Vrms × Irms",
                "PF = cosθ"
            ],
            'three_phase': [
                "Three-Phase Power Formulas:",
                "P = √3 × VL × IL × cosθ",
                "Q = √3 × VL × IL × sinθ",
                "S = √3 × VL × IL"
            ],
            'transformer': [
                "Transformer Formulas:",
                "Vp/Vs = Np/Ns = a",
                "Vs = Vp × (Ns/Np)"
            ],
            'motor': [
                "Three-Phase Motor Formulas:",
                "Nsync = (120×f)/P",
                "Slip = (Nsync - Nrotor)/Nsync × 100%",
                "T = 9.5488 × Pout/Nrotor",
                "IL = Pout/(√3×VL×cosθ×η)"
            ],
            'voltage_drop': [
                "voltage_drop Formulas:",
                "Single-phase: Vd = 2 × I × L × (Rcosθ + Xsinθ)",
                "Three-phase: Vd = √3 × I × L × (Rcosθ + Xsinθ)"
            ]
        }
        
        print("\n" + "="*40)
        for line in formulas.get(formula_name, []):
            print(line)
        print("="*40 + "\n")

    def ac_voltage_conversion(self):
        self.show_formula('ac_voltage')
        print("\n=== AC Voltage Conversion ===")
        print("1. Vpeak to Vrms")
        print("2. Vrms to Vpeak")
        choice = input("Select conversion (1-2): ")
        
        if choice == "1":
            v_peak = float(input("Enter peak voltage (V): "))
            v_rms = v_peak / math.sqrt(2)
            print(f"Vrms = {v_rms:.4f} V")
        elif choice == "2":
            v_rms = float(input("Enter RMS voltage (V): "))
            v_peak = v_rms * math.sqrt(2)
            print(f"Vpeak = {v_peak:.4f} V")
        else:
            print("Invalid choice!")

    def single_phase_power(self):
        self.show_formula('single_phase')
        print("\n=== Single-Phase Power Calculator ===")
        v = float(input("Voltage (Vrms): "))
        i = float(input("Current (Irms): "))
        theta = math.radians(float(input("Phase angle (degrees): ")))
        
        p = v * i * math.cos(theta)
        q = v * i * math.sin(theta)
        s = v * i
        pf = math.cos(theta)
        
        print("\nResults:")
        print(f"Real Power (P) = {p:.4f} W")
        print(f"Reactive Power (Q) = {q:.4f} VAR")
        print(f"Apparent Power (S) = {s:.4f} VA")
        print(f"Power Factor = {pf:.4f}")

    def three_phase_power(self):
        self.show_formula('three_phase')
        print("\n=== Three-Phase Power Calculator ===")
        vl = float(input("Line voltage (V): "))
        il = float(input("Line current (A): "))
        theta = math.radians(float(input("Phase angle (degrees): ")))
        
        p = self.sqrt3 * vl * il * math.cos(theta)
        q = self.sqrt3 * vl * il * math.sin(theta)
        s = self.sqrt3 * vl * il
        pf = math.cos(theta)
        
        print("\nResults:")
        print(f"Real Power (P) = {p:.4f} W")
        print(f"Reactive Power (Q) = {q:.4f} VAR")
        print(f"Apparent Power (S) = {s:.4f} VA")
        print(f"Power Factor = {pf:.4f}")

    def transformer_calc(self):
        self.show_formula('transformer')
        print("\n=== Transformer Calculator ===")
        vp = float(input("Primary voltage (V): "))
        np = int(input("Primary turns: "))
        ns = int(input("Secondary turns: "))
        
        vs = vp * (ns / np)
        a = np / ns
        
        print("\nResults:")
        print(f"Secondary voltage = {vs:.4f} V")
        print(f"Turns ratio (a) = {a:.4f}")

    def motor_calc(self):
        self.show_formula('motor')
        print("\n=== Three-Phase Motor Calculator ===")
        poles = int(input("Number of poles: "))
        freq = float(input("Supply frequency (Hz): "))
        rpm = float(input("Rotor speed (RPM): "))
        vl = float(input("Line voltage (V): "))
        hp = float(input("Motor power (HP): "))
        pf = float(input("Power factor: "))
        eff = float(input("Efficiency (%): ")) / 100
        
        # Calculations
        nsync = (120 * freq) / poles
        slip = (nsync - rpm) / nsync * 100
        pout = hp * 745.7  # Convert HP to watts
        pin = pout / eff
        il = pin / (self.sqrt3 * vl * pf)
        torque = 9.5488 * pout / rpm
        
        print("\nResults:")
        print(f"Synchronous speed = {nsync:.2f} RPM")
        print(f"Slip = {slip:.2f}%")
        print(f"Input current = {il:.4f} A")
        print(f"Torque = {torque:.4f} Nm")

    def voltage_drop(self):
        self.show_formula('voltage_drop')
        print("\n=== AC Voltage Drop Calculator ===")
        print("1. Single-phase: Vd = 2 × I × L × (Rcosθ + Xsinθ)")
        print("2. Three-phase: Vd = √3 × I × L × (Rcosθ + Xsinθ)")
        print("Where:")
        print("Vd = Voltage drop (V)")
        print("I = Current (A)")
        print("L = Length (m or ft)")
        print("R = Resistance per unit length (Ω/m or Ω/ft)")
        print("X = Reactance per unit length (Ω/m or Ω/ft)")
        print("θ = Phase angle (degrees)")
        print("="*50)
    
        system = input("Select system (1: Single-phase, 2: Three-phase): ")
        I = float(input("Current (A): "))
        L = float(input("Length (m): "))
        R = float(input("Resistance per unit length (Ω/m): "))
        X = float(input("Reactance per unit length (Ω/m): "))
        theta = math.radians(float(input("Phase angle (degrees): ")))
    
        impedance_component = R * math.cos(theta) + X * math.sin(theta)
    
        if system == "1":
            # Single-phase calculation
            Vd = 2 * I * L * impedance_component
            print(f"\nSingle-phase voltage drop: {Vd:.4f} V")
            print(f"Percentage drop: {(Vd/230)*100:.2f}% (based on 230V nominal)")
        elif system == "2":
            # Three-phase calculation
            Vd = math.sqrt(3) * I * L * impedance_component
            print(f"\nThree-phase voltage drop: {Vd:.4f} V")
            print(f"Percentage drop: {(Vd/400)*100:.2f}% (based on 400V nominal)")
        else:
            print("Invalid system selection!")

def main():
    calc = ElectricalCalculator()
    print("===== Electrical Engineering Calculator =====")
    print("Formulas will be displayed before each calculation\n")
    
    while True:
        print("\n===== Electrical Engineering Calculator =====")
        print("1. AC Voltage Conversion")
        print("2. Single-Phase Power Calculator")
        print("3. Three-Phase Power Calculator")
        print("4. Transformer Calculator")
        print("5. Three-Phase Motor Calculator")
        print("6. AC Voltage Drop Calculator")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")
        
        if choice == "1":
            calc.ac_voltage_conversion()
        elif choice == "2":
            calc.single_phase_power()
        elif choice == "3":
            calc.three_phase_power()
        elif choice == "4":
            calc.transformer_calc()
        elif choice == "5":
            calc.motor_calc()
        elif choice == "6":
            calc.voltage_drop()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
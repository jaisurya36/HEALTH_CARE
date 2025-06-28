from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class HealthApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # --- Food Check Section ---
        self.food_input = TextInput(hint_text='Enter food name', multiline=False)
        self.food_result = Label(text='Food Health Result')
        food_btn = Button(text='Check Food')
        food_btn.bind(on_press=self.check_food)

        # --- BMI Section ---
        self.weight_input = TextInput(hint_text='Enter weight (kg)', multiline=False, input_filter='float')
        self.height_input = TextInput(hint_text='Enter height (cm)', multiline=False, input_filter='float')
        self.bmi_result = Label(text='BMI Result')
        bmi_btn = Button(text='Calculate BMI')
        bmi_btn.bind(on_press=self.calculate_bmi)

        # --- Sugar Level Section ---
        self.sugar_input = TextInput(hint_text='Enter sugar level (mg/dL)', multiline=False, input_filter='float')
        self.sugar_result = Label(text='Sugar Level Result')
        sugar_btn = Button(text='Check Sugar')
        sugar_btn.bind(on_press=self.check_sugar)

        # --- Blood Pressure Section ---
        self.bp_sys_input = TextInput(hint_text='Enter systolic (top)', multiline=False, input_filter='int')
        self.bp_dia_input = TextInput(hint_text='Enter diastolic (bottom)', multiline=False, input_filter='int')
        self.bp_result = Label(text='BP Result')
        bp_btn = Button(text='Check BP')
        bp_btn.bind(on_press=self.check_bp)

        # --- Natural First Aid Section ---
        self.problem_input = TextInput(hint_text='Enter problem (e.g. headache)', multiline=False)
        self.problem_result = Label(text='Natural Remedy')
        remedy_btn = Button(text='Get Remedy')
        remedy_btn.bind(on_press=self.natural_remedy)

        # Add all widgets
        self.layout.add_widget(Label(text='💡 All-in-One Health Assistant', font_size=20))
        
        self.layout.add_widget(self.food_input)
        self.layout.add_widget(food_btn)
        self.layout.add_widget(self.food_result)

        self.layout.add_widget(self.weight_input)
        self.layout.add_widget(self.height_input)
        self.layout.add_widget(bmi_btn)
        self.layout.add_widget(self.bmi_result)

        self.layout.add_widget(self.sugar_input)
        self.layout.add_widget(sugar_btn)
        self.layout.add_widget(self.sugar_result)

        self.layout.add_widget(self.bp_sys_input)
        self.layout.add_widget(self.bp_dia_input)
        self.layout.add_widget(bp_btn)
        self.layout.add_widget(self.bp_result)

        self.layout.add_widget(self.problem_input)
        self.layout.add_widget(remedy_btn)
        self.layout.add_widget(self.problem_result)

        return self.layout

    # --- Food Check Logic ---
    def check_food(self, instance):
        food = self.food_input.text.lower()
        if food in ['apple', 'banana','beetroot','pomegranate','carrot', 'oats','orange','badam','pista','fig','dates','almond','yogurt','avocado','green tea','cucumber','sweet potato','potato','brown rice','berries','greens','nuts','ground nut']:
            self.food_result.text = "✅ Healthy Food"
        elif food in ['burger', 'pizza', 'chips', 'soda','fried chicken','soft drinks','ice cream','processed meat','french fries','white breaad','candy','sugar','puffs','oily snacks']:
            self.food_result.text = "❌ Unhealthy Food. Try fruits or salad!"
        elif food in ['rice', 'paneer', 'milk','egg','pasta','noodles','cornflakes','butter','ghee','chocolates','idli','dosa']:
            self.food_result.text = "⚠️ Moderate – eat in balanced amounts"
        else:
            self.food_result.text = "Food not in database."

    # --- BMI Calculation Logic ---
    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height_cm = float(self.height_input.text)
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)

            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 25:
                status = "Normal"
            elif 25 <= bmi < 30:
                status = "Overweight"
            else:
                status = "Obese"

            self.bmi_result.text = f"BMI: {bmi:.1f} – {status}"
        except:
            self.bmi_result.text = "Please enter valid height and weight."

    # --- Sugar Check Logic ---
    def check_sugar(self, instance):
        try:
            sugar = float(self.sugar_input.text)
            if sugar < 70:
                self.sugar_result.text = "Low Sugar – Hypoglycemia risk."
            elif 70 <= sugar <= 140:
                self.sugar_result.text = "Normal Sugar Level."
            elif 140 < sugar <= 199:
                self.sugar_result.text = "Prediabetic Stage."
            else:
                self.sugar_result.text = "High Sugar – Diabetes Risk!"
        except:
            self.sugar_result.text = "Invalid sugar input."

    # --- Blood Pressure Check Logic ---
    def check_bp(self, instance):
        try:
            sys = int(self.bp_sys_input.text)
            dia = int(self.bp_dia_input.text)
            if sys < 90 or dia < 60:
                self.bp_result.text = "Low Blood Pressure"
            elif sys <= 120 and dia <= 80:
                self.bp_result.text = "Normal Blood Pressure"
            elif sys > 140 or dia > 90:
                self.bp_result.text = "High Blood Pressure"
            else:
                self.bp_result.text = "Slightly Elevated"
        except:
            self.bp_result.text = "Invalid BP input."

    # --- Natural First Aid Remedy Logic ---
    def natural_remedy(self, instance):
        problem = self.problem_input.text.lower()
        if problem == "headache":
            self.problem_result.text = "🧠 Rest in a quiet room, drink water."
        elif problem == "stomach pain":
            self.problem_result.text = "🍌 Eat banana, drink warm water."
        elif problem == "cold":
            self.problem_result.text = "☕ Steam inhalation and warm fluids."
        elif problem == "fever":
            self.problem_result.text = "🛌 Rest, sponge bath with lukewarm water."
        elif problem == "cough":
            self.problem_result.text = "🍯 Try honey with warm water."
        else:
            self.problem_result.text = "Try rest, hydration or consult a doctor."

# Run the app
HealthApp().run()

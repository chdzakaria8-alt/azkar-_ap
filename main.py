from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class AzkarApp(App):
    def build(self):
        # تنظيم العناصر عمودياً داخل واجهة التطبيق
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # نص ترحيبي علوي للمستخدم
        self.label = Label(text="مرحباً بك في تطبيق الأذكار اليومية", font_size='22sp')
        layout.add_widget(self.label)
        
        # زر مخصص لأذكار الصباح
        btn1 = Button(text="أذكار الصباح", size_hint=(1, 0.2), background_color=(0, 0.6, 0, 1))
        btn1.bind(on_press=self.show_morning)
        layout.add_widget(btn1)
        
        # زر مخصص لأذكار المساء
        btn2 = Button(text="أذكار المساء", size_hint=(1, 0.2), background_color=(0, 0.4, 0.8, 1))
        btn2.bind(on_press=self.show_evening)
        layout.add_widget(btn2)
        
        return layout

    def show_morning(self, instance):
        self.label.text = "أصبحنا وأصبح الملك لله والحمد لله"

    def show_evening(self, instance):
        self.label.text = "أمسينـا وأمسى الملك لله والحمد لله"

if __name__ == '__main__':
    AzkarApp().run()


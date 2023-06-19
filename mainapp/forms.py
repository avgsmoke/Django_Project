from django.forms import forms, ModelForm

from mainapp.models import FeedBack


class FeedbackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['placeholder'] = 'Адресс объекта недвижимости: '
        self.fields['product'].widget.attrs['placeholder'] = 'Выберите продукт для заказа: '
        self.fields['full_name'].widget.attrs['placeholder'] = 'ФИО: '
        self.fields['tel'].widget.attrs['placeholder'] = 'Телефон: '
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail: '
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            field.label = ''


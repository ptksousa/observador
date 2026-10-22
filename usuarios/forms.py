from django import forms

class CadastroForms(forms.Forms):
    usuario=forms.CharField(
        label="Usuario",
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex.: O Observador"
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ex.: observador@email.com"
            }
        )
    )
    senha_1=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label="Confirme a senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
         nome = self.cleaned_data.get("nome_cadastro")

         if nome:
             nome = nome.strip()
             if " " in nome:
                 raise forms.ValidationError("Não é possível inserir espaços dentro do campo Nome de Cadastro")
             else:
                 return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são iguais.")
            else:
                return senha_2
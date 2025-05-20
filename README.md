# 📋 PlanilhasRCM

Sistema para controle de serviços, com cadastro de serviços, registros de execução, exportação de relatórios e interface moderna baseada em AdminLTE.

---

## 🚀 Funcionalidades

- Cadastro e edição de serviços com unidade de medida e escopo mínimo
- Registro de execução de serviços, com upload de fotos e observações
- Listagem detalhada de registros e serviços
- Exportação de registros para Excel (.xlsx) usando Pandas e Openpyxl
- Interface responsiva e intuitiva com AdminLTE
- Controle de acesso por autenticação de usuário

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [AdminLTE (via template)](https://adminlte.io/)
- [Bootstrap 4](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/RafaelCirn3/PlanilhasRCM.git
cd PlanilhasRCM
```
### 2. Crie um ambiente virtual

```bash
python -m venv venv
```
### 3. Ative o ambiente virtual
- No Windows:

```bash
./venv/Scripts/activate
```
- No Linux/Mac:

```bash
source .venv/bin/activate
```
### 4. Instale as dependências

```bash
pip install -r requirements.txt
```
### 5. Crie o banco de dados

```bash
python manage.py migrate
```
### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```
### 7. Inicie o servidor

```bash
python manage.py runserver
```
### 8. Acesse o sistema
Abra o navegador e acesse `http://127.0.0:8000/`

### 9. Acesse o admin
Acesse o admin em `http://127.0.0:8000/admin/` e faça login com o superusuário criado.

### 10. Acesse o sistema
após realizar o login, você terá acesso ao sistema, onde poderá cadastrar serviços, registrar execuções e exportar relatórios.

### Exportação de relatórios
Para exportar os registros de execução, acesse a página de listagem de registros e clique no botão "Exportar para Excel". O arquivo será gerado e baixado automaticamente.

### Observações
- O sistema utiliza o banco de dados SQLite por padrão. Para usar outro banco de dados, altere as configurações no arquivo `settings.py`.
- O sistema foi desenvolvido e testado com Python 3.12 e Django 5.x. Versões anteriores podem não funcionar corretamente.
- O sistema salva as fotos no diretório `media/execucoes/`. Certifique-se de que esse diretório exista e tenha permissão de escrita.

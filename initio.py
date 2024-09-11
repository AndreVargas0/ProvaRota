@app.route('/novocliente')
def cadastrar_cliete():
    nome = request.form['nome']
    telefone = int(request.form['telefone'])
    email = request.form['email']
    senha = request.form['senha']
    
 
    cliente = cliente(nome=nome, telefone=telefone,email=email,senha=senha)
    try:
      session.add(cliente) 
      session.commit()
    except:
      session.rollback()
      raise
    finally:
       session.close()
    mensagem = f"Cadastro do cliente {nome} efetuado com sucesso!"   

@app.route('/novoservico')
def cadastrar_servico():
    servico = request.form['servico']
    valor = request.form['valor']
    novoservico = novoservico(servico=servico, valor=valor)
    try:
      session.add(novoservico) 
      session.commit()
    except:
      session.rollback()
      raise
    finally:
       session.close()
    mensagem2 = f"O {servico} foi cadastrado com sucesso no sistemas!"   
    return render_template('cadastro.html', mensagem2=mensagem2)


@app.route('/novoagendamento')
def novo_agendamento():
    data = request.form['data']
    hora = request.form['hora']
    cliente = request.form['cliente']
    servico = request.form['servico']
    funcionario = request.form['funcionario'] 
    novoagendamento = novoagendamento(data=data, hora=hora,cliente=cliente,servico=servico,funcionario=funcionario)
    try:
      session.add(agendamento) 
      session.commit()
    except:
      session.rollback()
      raise
    finally:
       session.close() 
    mensagem3 = f"O {servico} foi agendado para o dia {data}, horário {hora} com o(a) {funcionario}!"   
    return render_template('agendamento.html', mensagem3=mensagem3)



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        usuario = usuario.query.filter_by(email=email).first()
        if usuario and usuario.senha == senha:
            login_usuario(usuario)
            mensagem4= 'Login feito com sucesso!'
            return render_template('home.html', mensagem4=mensagem4)
        else:
            mensagem5='Email ou senha errado'
            return render_template('login.html', mensagem5=mensagem5)


@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

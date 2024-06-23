class Heroi {
    constructor(nome, idade, tipo){
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }

    atacar(){
        let ataque ="as mãos"

        if (this.tipo === "mago") {
            ataque = "magia";
        }else if (this.tipo === "guerreiro") {
            ataque = "espada";
        }else if (this.tipo === "monge") {
            ataque = "artes marciais";
        }else if (this.tipo === "ninja") {
            ataque = "shuriken";
        }

        console.log(`O ${this.tipo} atacou usando ${ataque}`)

    }
}

   var heroi = new Heroi("Dulan Stone", 23, "guerreiro");

    heroi.atacar();



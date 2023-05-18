import { useRouter } from 'next/router';

const usuarios = {
    1:{
        nome: "Yan Martins"
    },
    2:{
        nome: "Luiz Estevão"
    },
    3:{
        nome: "Vicente Calfo"
    }
}

export default function Usuario(){
    const router = useRouter();
    const {id} = router.query;
    return (
        <>
            <h1>Usuário selecionado: {usuarios[id].nome}</h1>
        </>
    )
}
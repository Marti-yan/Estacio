import Link from 'next/link';
import styles from '../styles/usuarios.module.css'

const usuarios = [
    {
        nome: "Yan Martins",
        id: 1
    },
    {
        nome: "Luiz Estevão",
        id: 2
    },
    {
        nome: "Vicente Calfo",
        id: 3
    }
]

export default function Usuarios(){
    return (
        <>
            <h1>Lista Usuários</h1>
            {
                usuarios.map(usuario => (
                    <Link href={`/usuario/${usuario.id}`}>
                        <h2 className={styles.card}>{usuario.nome}</h2>
                    </Link>
                ))
            }
        </>
    )
}
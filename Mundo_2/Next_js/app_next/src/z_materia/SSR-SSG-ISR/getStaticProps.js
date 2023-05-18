// Para realizar uma renderização de sites estáticos, o Next.js permite a exportação de uma função chamada getStaticProps de um componente que seja uma página.

// Os usuários serão gerados na lista em tempo de criacão (build) pela função getStaticProps()
function Usuarios({ usuarios }) {
    return (
        <ul>
        {usuarios.map((usuario)=>(
            <li>{usuario.nome}</li>
        ))}
      </ul>
    )
}
    
// Esta função será chamada em tempo de construção (build) no lado do servidor
export async function getStaticProps() {
    // Chamando API externa para trazer os usuários do sistema.
    const res = await fetch('https: //exemplo.api/v2/usuarios')
    const usuarios = await res.json( )
    // Retornando a lista de usuários da API para ser enviado a componente de página Usuarios
    return {
        props: {
            usuarios,
        },
    }
}
export default Usuarios
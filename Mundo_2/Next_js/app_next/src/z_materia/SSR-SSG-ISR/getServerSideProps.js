// A função getServerSideProps só funcionará se for exportada de um componente que seja uma página, como evidencia o exemplo a seguir:
function Pagina({ data }) {
    // Renderiza os dados da página...
}

// A função getServerSideProps será chamada a cada requisição
export async function getServerSideProps() {
    // Buscando dados externos em uma API
    const res = await fetch(`https://api.exemplo.to/v2/dados`)
    const data = await res. json()
    // Passando os dados recuperados para a página (Pagina) via props
    return { props: { data } }
}

export default Pagina
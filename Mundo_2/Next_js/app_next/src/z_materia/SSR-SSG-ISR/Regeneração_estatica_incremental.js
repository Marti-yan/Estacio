//  abordagem incremental é bem parecida com a renderização SSG, tendo inclusive a mesma função. A getStaticProps, porém, tem um parâmetro a mais, como veremos no pedaço de código a seguir:


function Noticias({ noticias }) {
    return (
        <ul>
            {noticias.map((noticia) => (
                <li key={noticia.id}>{noticia.titulo}</li>
            ))}
        </ul>
    )
}

// Esta função vai ser chamada em tempo de construção (build), e poderá ser chamada também se a revalidação estiver ativa
export async function getStaticProps() {
    const res = await fetch('https://exemplo.api.io/v2/noticias')
    const noticias = await res.json()

    return {
        props: {
            noticias,
        },
        // O NEXT.JS vai tentar regenerar a pagina quando:
        // - Uma requisição for feita
        // - A cada 10 segundos
        revalidate: 10, // em segundos
    }
}

// Esta função vai ser chamada em tempo de construção (build)
export async function getStaticPaths() {
    const res = await fetch('https://exemplo.api.io/v2/noticias')
    const noticias = await res.json()

    // Obtem os caminhos que desejamos pre-renderizar com base nas notícias recuperadas via API

    const paths = noticias.map((noticia) => ({
        params: { id: noticia.id },
    }))

    // As páginas serão geradas com base nesses caminhos (paths) recuperados via API
    // parametro (fallback: 'blocking'}, permite que sob demanda as páginas sejam geradas quando o caminho não existir previamente
    return { paths, fallback: 'blocking' }
}

export default Noticias
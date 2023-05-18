import { withRouter } from 'next/router';

const NoticiasQueryString = withRouter((props) => {
    return (
        <>
            <h1>Página Query</h1>
            <p>Ano da noticia: {props.router.query.ano}</p>
            <p>Categoria: {props.router.query.categoria}</p>

        </>
    )
})

export default NoticiasQueryString;
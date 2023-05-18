
import styles from './page.module.css'
import Link from "next/link"
import buscarNoticias from '../lib/noticias'

const Home = () => ({ noticias }) => {
  return(
  <>
    <h1>Notícias</h1>
    <ul>
      {noticias.map(({ slug, title }) => (
        <li key={slug}>
          <Link href={`/${slug}`}>
            {title}
          </Link>
        </li>
      ))}
    </ul>
  </>
  )
};

export async function getStaticProps(){
  return{
    props: {
      noticias: await buscarNoticias()
    }
  }
}

export default Home

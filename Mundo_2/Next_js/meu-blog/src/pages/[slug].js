import { ReactMarkdown} from "react-markdown/lib/react-markdown";
import buscarNoticias from "../lib/noticias";


const Noticia = ({ title, date, markdown }) => (
    <article> 
      <h1>{title}</h1>
      <time>{date}</time>
      <ReactMarkdown>{markdown}</ReactMarkdown>
    </article>
  );
  
  export const getStaticPaths = async () => {
      const noticias = await buscarNoticias();
  
      return {
          paths: noticias.map((noticia)=> '/${noticia.slug}'),
          fallback: false,
      };
  };
  
  export const getStaticProps = async ({ params: { slug } }) => {
      const noticias = await buscarNoticias();
      const noticia = noticias. find ((noticia) => noticia.slug === slug);
      
      return { props: noticia};
  };
  
  export default Noticia;
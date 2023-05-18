import Link from 'next/link'
import styles from './page.module.css'
import Image from 'next/image'
import foto from '../../public/assets/yan.jpg'
import build from 'next/dist/build'

export default function Home() {
  return (
    < >
      <Link href="/usuarios" >
        <button className={styles.button}>Lista de Usuários</button>
      </Link>
      <br />
      <hr />
      <div className={styles.foto}>
        <div >
          <Image  // Carregando a Imagem local (no arquivo por causa o 'import')
            src={foto}
            alt="Foto deveria estar aqui"
            //     -- nesse caso eu não preciso informar o tamanho da IMG...
            // width={250}
            // height={400}
            blurDataURL="data" //para manter a imagem borrada, enquanto a imagem original tem seu carregamento finalizado.
            placeholder="blur" // Opcional para borrar a imagem enquanto o carregamento ocorre
          />
        </div>
        <br />
        <hr />
        <br />
        <Image
          src="/assets/yan2.jpg"
          alt="Foto deveria estar aqui"
          //  -- ... Ja aqui se eu não informar o tamanho da img da erro
          width={250}
          height={400}
        />
      </div>

    </>
  )
}

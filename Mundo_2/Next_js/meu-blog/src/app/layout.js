// import Head from 'next/head';
import Home from './page'

function MyApp({ Component, pageProps}){
  return(
    <>
      {/* <Head>
        <title>Meu Blog aaa</title>
        <link rel="icon" href="/favicon.ico" />
      </Head> */}
      <h1>ta aqui</h1>
      <Home />
      {/* <Component {...pageProps} /> */}
    </>
  )
}
export default MyApp
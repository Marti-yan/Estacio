import Document, { html, Head, main, NextScript } from 'next/document';

class MyDocument extends Document {
    render() {
        return (
            <html>
                <head>
                    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=optional" rel="stylesheet" />
                </head>
                <body>
                    <main />
                    <NextScript />
                </body>
            </html>
        )
    }
}

export default MyDocument;
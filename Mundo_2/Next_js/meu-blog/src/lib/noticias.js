import { promises as fs } from 'fs'
import path from "path"
import matter from "gray-matter"

const buscarNoticias = async () => {
    const diretorioNoticias = path.join(process.cwd(), "noticias");
    const fileNames = await fs.readdir(diretorioNoticias);

    return await Promisse.all(
        fileNames.map(async (fileName) => {
            const filePath = path.join(diretorioNoticias, fileName);
            const fileContents = await fs.readFile(filePath, 'utf8');
            const document = matter(fileContents);

            return{
                slug: fileName.replace(/\.md$/,""),
                title: document.data.title,
                date: document.data.date,
                markdown: document.content
            }
        })
    )
}
export default buscarNoticias;
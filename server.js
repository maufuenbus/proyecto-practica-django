const PORT = process.env.PORT || 3000;
const express = require('express');
const app = express();

const path = require('path');
const multer = require('multer'); // ayuda a gestionar los files.


let storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, './media')
    },
    filename: (reg, file, cb) => {
        cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
    }
});

const upload = multer({ storage });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    return res.send('prueba');
});

app.post('/subir', upload.single('file'), (req, res) => {
    console.log(`prueba es ${req.hostname} / ${req.file.path}`);
    return res.send(req.file);
});

app.listen(PORT, () => console.log(`prueba funciona: ${PORT}`));
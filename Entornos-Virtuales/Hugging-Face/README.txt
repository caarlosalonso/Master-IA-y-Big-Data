# Masterclass de Hugging Face

Hola familia! Este es el material de la clase sobre Hugging Face.

## Qué hay aquí

Este repo tiene todo lo que necesitas para empezar a trabajar con Hugging Face desde cero:

- **masterclass_huggingface.ipynb**: El notebook principal con toda la teoría y ejemplos. Tiene TODO lo que vimos en clase más algunos ejemplos extra por si quieres profundizar.

- **requirements.txt**: Lista de todas las librerías que necesitas instalar. Spoiler: son bastantes, pero casi todas se instalan solas cuando instalas transformers.

- **INSTALACION.md**: Guía paso a paso de cómo instalar todo. Si tienes problemas con la instalación (que suele pasar), aquí están las soluciones a los errores más comunes.

## Cómo empezar

### Si nunca has instalado nada de esto:

1. Abre una terminal/cmd
2. Crea un entorno virtual (en serio, hazlo, te va a ahorrar muchos dolores de cabeza):
   ```
   python -m venv venv_hf
   ```
3. Actívalo:
   - Windows: `venv_hf\Scripts\activate`
   - Mac/Linux: `source venv_hf/bin/activate`
4. Instala todo:
   ```
   pip install -r requirements.txt
   ```
5. Abre Jupyter:
   ```
   jupyter notebook
   ```
6. Abre el notebook masterclass_huggingface.ipynb y a correr!

### Si ya tienes Jupyter y PyTorch instalados:

Probablemente solo necesites:
```
pip install transformers huggingface-hub
```

Y ya está, el notebook debería funcionar.

## Cosas importantes que hay que saber

**La primera vez que ejecutes un modelo va a tardar**: Hugging Face descarga los modelos automáticamente y algunos pesan bastante (hasta 1-2 GB). Se guardan en tu caché y la próxima vez va más rápido.

**Si no tienes GPU**: No pasa nada, todos los ejemplos funcionan en CPU. Van a ser un poco más lentos pero nada dramático para los ejemplos del notebook.

**Si algo no funciona**: Revisa primero el archivo INSTALACION.md que tiene soluciones a los errores típicos. Si sigue sin funcionar, escríbeme.

## Qué vas a aprender

El notebook está dividido en 5 partes:

1. **Qué es Hugging Face**: Contexto y por qué es útil (con ejemplos de empresas reales que lo usan)

2. **Cómo buscar modelos**: Tanto manualmente como con código. Hay más de 500K modelos, hay que saber encontrar el que necesitas.

3. **Pipelines**: La forma más fácil de usar modelos. Ideal para prototipos rápidos.

4. **Sintaxis básica**: Cómo usar cualquier modelo, ya sea con pipeline o manualmente. Esto es lo más importante.

5. **7 ejemplos prácticos**: 
   - Análisis de sentimiento (tipo reviews de productos)
   - Named Entity Recognition (extraer nombres, lugares, organizaciones)
   - Question Answering (sistemas de FAQ)
   - Traducción automática
   - Fill-mask (autocompletado)
   - Implementación manual con clase propia
   - Manejo de errores (porque siempre hay que validar inputs)

## Ejercicios

Al final del notebook hay 3 ejercicios propuestos. Están ordenados de más fácil a más difícil. Te recomiendo que intentes hacerlos porque es la mejor forma de aprender.

## Recursos extra

Si quieres profundizar más:
- Documentación oficial: https://huggingface.co/docs/transformers
- Model Hub: https://huggingface.co/models (aquí están todos los modelos)
- Course gratis de Hugging Face: https://huggingface.co/course (está muy bien, muy recomendado)

## Tips random que te van a servir

- Los modelos "distil" (distilbert, distilgpt2, etc.) son versiones más pequeñas y rápidas. Úsalos para prototipar.

- Para español, busca modelos que tengan "beto", "robertuito" o "spanish" en el nombre.

- Si un modelo tarda mucho, prueba con batch_size más pequeño o un modelo distil.

- La documentación de Hugging Face es muy buena, pero a veces está en inglés. Vale la pena leerla.

- No te obsesiones con tener la última versión de todo. Si algo funciona, déjalo así.

## Troubleshooting rápido

**"No module named transformers"**
→ pip install transformers

**"CUDA out of memory"**
→ Usa device="cpu" o modelos más pequeños

**Tarda mucho en la primera ejecución**
→ Normal, está descargando el modelo. Hazte un café.

**Error raro con tokenizers en Windows**
→ pip install tokenizers --no-cache-dir

**El modelo dice cosas raras**
→ Asegúrate de que el texto esté en el mismo idioma que el modelo fue entrenado

## Notas finales

Este es material de clase, así que si encuentras errores o algo que no queda claro, avísame y lo actualizo.

Los ejemplos están pensados para que sean prácticos y útiles. No son perfectos ni están optimizados al máximo, pero funcionan y muestran los conceptos importantes.

Acuérdate de que lo importante no es memorizar toda la sintaxis, sino entender CÓMO funciona Hugging Face y saber buscar el modelo que necesitas para tu proyecto.

Cualquier duda, pregunta!

---

Última actualización: Noviembre 2025
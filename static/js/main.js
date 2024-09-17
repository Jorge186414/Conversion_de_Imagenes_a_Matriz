// Obtener el formulario y añadirle un evento de submit
document.getElementById('upload-form').addEventListener('submit', event => {
  event.preventDefault()

  var formData = new FormData()
  var fileInput = document.getElementById('archivo')

  if (fileInput.files.length === 0) {
    alert('Por favor carga una imagen')
    return
  }

  formData.append('archivo', fileInput.files[0])

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {

      if (data.error) {
        alert(data.error)
        return
      }

      var imagen_original = document.getElementById('imagen_original')
      imagen_original.src = '/static/images/' + data.Imagen_Original
      imagen_original.style.display = 'block'

      var imagen_blanco_negro = document.getElementById('imagen_blanco_negro')
      imagen_blanco_negro.src = '/static/images/' + data.Imagen_Blanco_Negro
      imagen_blanco_negro.style.display = 'block'

      const matriz = data.Matriz_de_Imagen

      var matriz_corta = matriz.slice(0, 1)

      var resultado = document.getElementById('resultado')
      resultado.style.display = 'block';

      var matriz_resultante =
        `<p>${JSON.stringify(matriz_corta, null, 2)}</p>`

      document.getElementById('contenedor_matriz').innerHTML = matriz_resultante
    })
    .catch(error => console.error('ERROR', error))
})

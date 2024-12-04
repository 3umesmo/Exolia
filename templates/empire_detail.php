<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detalhes do Império: {{ empire }}</title>
</head>
<body>
    <h1>Império: {{ empire_name }}</h1>
    <h2>Planetas controlados: </h2>
    <ul>
        <?php
            print {{listaPlanetas}}
        
    </ul>
    <a href="create_planet?empire_name={{empire_name}}">Adicionar planeta</a>
</body>
</html>
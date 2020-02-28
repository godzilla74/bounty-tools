<html>
<head>
    <title>Redirect based on parameter</title>
</head>
<body>
    <h1>Redirect based on incoming url param</h1>

    <?php
//        echo $_GET["url"];
        header("Location: http://" . $_GET["url"]);
    ?>

</body>
</html>

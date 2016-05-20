<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <!--    <title>这是对稀客网站的爬虫程序</title>-->
</head>
<div>
    <!--    <p>这是对稀客网站的爬虫宝具</p>-->
</div>
<div>
    <form action="" method="post">
        开始<input type="submit" name="button" value="提交"/>
    </form>
</div>
<?php
//post获取内容
function request_by_curl($remote_server, $post_string)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $remote_server);
    curl_setopt($ch, CURLOPT_SAFE_UPLOAD, true);
    curl_setopt($ch, CURLOPT_POST, true);//post提交方式
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post_string);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    $data = curl_exec($ch);
    curl_close($ch);
    return $data;
}


//筛选图片地址
function filterurl($web_content)
{
    //$match_result = array();
    $reg_tag_a = '{"id":(.*?),"url":"(.*?)","upload_time":".*?"}';
    $result = preg_match_all($reg_tag_a, $web_content, $match_result);
    if ($result) {
        return $match_result;
    }
}

//保存文件
function save_file($path, $url)
{
    $img = file_get_contents($url);
    echo $path;
    echo $url;
    file_put_contents($path, $img);
    echo '<img src = ' + $path + '>';
}

$post_data = array(
    "cache" => '{"id":0,"cacheid":""}',
    "oper" => 'listimages',
    "data" => '{"pageIndex":0,"folderId":0}'
);
//echo print_r($post_data, 1);
$post = http_build_query($post_data);
$url = 'http://prprleg.com/Mprpr/m';
$res = request_by_curl($url, $post);
$imgdata = filterurl($res);
//echo print_r($imgdata[1], 1);

if (!empty($_POST['button'])) {
//    for ($x = 0; $x < count($imgdata[1]); $x++) {
//        echo $imgdata[1][$x] . ",";
//        ob_flush();
//        flush();
//        sleep(1);
//        //save_file("/prpr/" . $imgdata[1][$x] . ".jpg", "http://cdn.img.prprleg.com/" . $imgdata[2][$x]);
//    }
    for ($i = 0; $i < 20; $i++) {
        echo "lalallala," . "<br>";
        ob_flush();
        flush();
        sleep(1);
    }
}


?>


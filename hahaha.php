<!--<!DOCTYPE html>-->
<!--<head>-->
<!--    <meta charset="UTF-8">-->
<!--    <title>这是对稀客网站的爬虫程序</title>-->
<!--</head>-->
<!--<div>-->
<!--    <p>这是对稀客网站的爬虫宝具</p>-->
<!--</div>-->
<!--<div>-->
<!--    URL:<input type="text" name="url"/>-->
<!--    保存地址:<input type="text" name="localUrl"/>-->
<!--</div>-->
<?php
/*
function request_post($url = '', $param = '')
{
    if (empty(empty($url)) || empty($param)) {
        return false;
    }
    $postUrl = $url;
    $curlPost = $param;
    $ch = curl_init();//初始化curl
    curl_setopt($ch, CURLOPT_URL, $postUrl);//抓取指定网页
    curl_setopt($ch, CURLOPT_HEADER, 0);//
    curl_setopt($ch, CURLOPT_HTTPHEADER,
        Array('Content-Type:application/x-www-form-urlencoded; charset=UTF-8',
            'Host:prprleg.com',
            'Origin:http://www.prprleg.com',
            'Referer:http://www.prprleg.com/',
            'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        ));//设置header
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);//要求结构为字符串
    curl_setopt($ch, CURLOPT_POST, 1);//post提交方式
    curl_setopt($ch, CURLOPT_POSTFIELDS, $curlPost);//data数据
    $data = curl_exec($ch);
    return $data;
}

$url = 'http://mobile.jschina.com.cn/jschina/register.php';
$post_data = array(
    'cache' => array(
        'id' => 0,
        'cacheid' => ""
    ),
    'data' => array(
        'pageIndex' => 0,
        'folderId' => 0
    ),
    'open' => "listimages"
);

$res = request_post($url, $post_data);

echo $res;
 */

function request_by_curl($remote_server, $post_string)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $remote_server);
    curl_setopt($ch, CURLOPT_SAFE_UPLOAD, true);
    curl_setopt($ch, CURLOPT_POST, true);//post提交方式
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post_string);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HEADER, 0);
//    curl_setopt($ch, CURLOPT_HTTPHEADER,
//        Array(
//            'Host:www.atool.org',
//            'Origin:http://www.atool.org',
//            'Referer:http://www.atool.org/httptest.php',
//            'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
//        ));//设置header
    $data = curl_exec($ch);
    curl_close($ch);

    return $data;
}

$post_data = array(
    "cache" => '{"id":0,"cacheid":""}',
    "oper" => 'listimages',
    "data" => '{"pageIndex":0,"folderId":0}'
);
//echo print_r($post_data, 1);
$post = http_build_query($post_data);
//echo $post;
$url = 'http://prprleg.com/Mprpr/m';
$res = request_by_curl($url, $post);
echo $res;

?>


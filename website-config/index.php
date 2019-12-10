<?php
/*
 * This script is put at the website main page.
 */
$settings = array();

if(is_dir('iml')) {
  $settings['ieel']['url'] = 'https://' . $_SERVER['HTTP_HOST'] . '/iml';
  $settings['ieel']['image'] = './IntelLogo.png';
  $settings['ieel']['title'] = 'Intel(R) Manager for Lustre';
}

if(is_dir('openstack')) {
  $settings['openstack']['url'] = 'http://' . $_SERVER['HTTP_HOST'] . ':10080/';
  $settings['openstack']['image'] = './Bright-Openstack.png';
  $settings['openstack']['title'] = 'Bright OpenStack';
}

if(is_dir('lab2cnew')) {
  $settings['lab2cnew']['url'] = 'http://' . $_SERVER['HTTP_HOST'] . '/lab2cnew';
  $settings['lab2cnew']['image'] = './hugo.svg';
  $settings['lab2cnew']['title'] = 'Lab Website';
}

if(is_dir('elk')) {
  $settings['elk']['url'] = 'https://' . $_SERVER['HTTP_HOST'] . ':5602/app/kibana#/dashboard/Default';
  $settings['elk']['short_url'] = 'https://' . $_SERVER['HTTP_HOST'] . ':5602/app/kibana';
  $settings['elk']['image'] = './elk.png';
  $settings['elk']['title'] = 'Elasticsearch/Logstash/Kibana';
}

if(is_dir('mesos')) {
  $settings['mesos']['url'] = 'https://' . $_SERVER['HTTP_HOST'] . ':8082';
  $settings['mesos']['image'] = './MesosLogo.png';
  $settings['mesos']['title'] = 'Mesos';
}

if(is_dir('marathon')) {
  $settings['marathon']['url'] = 'https://' . $_SERVER['HTTP_HOST'] . '/marathon';
  $settings['marathon']['image'] = './MarathonLogo.png';
  $settings['marathon']['title'] = 'Marathon';
}
$settings['wiki']['url'] = 'http://' . $_SERVER['HTTP_HOST'] . '/wiki';
$settings['wiki']['image'] = './mediawikiwiki.png';
$settings['wiki']['title'] = 'Wiki';

$settings['thinlinc']['url'] = 'https://' . $_SERVER['HTTP_HOST'] . ':300';
$settings['thinlinc']['image'] = './thinlinc.jpg';
$settings['thinlinc']['title'] = 'Remote Desktop'; 

$settings['gitlab']['url'] = 'http://' . $_SERVER['HTTP_HOST'] . ':88';
$settings['gitlab']['image'] = './gitlab.jpg';
$settings['gitlab']['title'] = 'Gitlab';

$settings['jupyter']['url'] = 'https://' . $_SERVER['HTTP_HOST'] . ':8000';
$settings['jupyter']['image'] = './jupyter.jpg';
$settings['jupyter']['title'] = 'Jupyter';

$settings['seafile']['url'] = 'http://' . $_SERVER['HTTP_HOST'] . ':8030';
$settings['seafile']['image'] = './seafile-logo.png';
$settings['seafile']['title'] = 'Seafile';

?>
<html>
  <head>
    <title>Bright Cluster Manager landing page</title>
<?php
if(count($settings)==1) {
  reset($settings);
  $key = key($settings);
?>
    <meta http-equiv="refresh" content="0; url=<?php echo $settings[$key]['url'];?>" />
<?php
} else {
?>
    <link rel="stylesheet" type="text/css" href="main.css">
    <link rel="stylesheet" type="text/css" href="bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="main.css">
<?php
}
?>
  </head>
  <body>
<?php
if(count($settings)!=1) {
?>
    <img src="Bright-splash.png" id="bg" alt="">
    <div style="padding-top: 50px;"></div>
    <div class="container">
<?php
  foreach ($settings as $key => $value) {
?>
      <div class="col-md-5 well">
        <div class="row">
          <div class="col-md-12">
            <h1><?php echo $value['title'];?></h1>
          </div>
        </div>
        <div class="row">
          <div class="col-md-3">
            <img border="0" src="<?php echo $value['image'];?>" width="100" height="100">
          </div>
          <div class="col-md-9">
            <a href="<?php echo $value['url'];?>"><?php echo (isset($value['short_url']) ? $value['short_url']  :  $value['url']); ?></a>
          </div>
        </div>
      </div>

      <div class="col-md-1"></div>
<?php
  }
?>

<?php
}
?>
  </body>
</html>

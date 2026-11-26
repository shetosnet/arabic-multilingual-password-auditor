<?php
// Analyze one password.   ZYLA_API_KEY=... php analyze.php 'Ahmed@01012345678'
$url = getenv('PA_ANALYZE_URL') ?: 'https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities';
$key = getenv('ZYLA_API_KEY') ?: '';
$password = $argv[1] ?? null;
if ($password === null) { fwrite(STDERR, "Usage: php analyze.php <password>\n"); exit(1); }

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 15,
    CURLOPT_HTTPHEADER => ['Authorization: Bearer ' . $key, 'Content-Type: application/json'],
    CURLOPT_POSTFIELDS => json_encode(['password' => $password, 'check_cloud' => false], JSON_UNESCAPED_UNICODE),
]);
$body = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
curl_close($ch);
if ($body === false || $code !== 200) { fwrite(STDERR, "Request failed (HTTP $code)\n"); exit(1); }

$data = json_decode($body, true);
echo "{$data['status']} (score {$data['score']}/100)\n";
foreach ($data['vulnerabilities'] as $v) { echo " - $v\n"; }

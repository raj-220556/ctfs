#!/usr/bin/env bash


$data=$(cat server.log | grep "INFO FLAGPART: ");

echo $data;



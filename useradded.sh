#!/bin/bash
do

    sudo groupadd -g 2005 RestrictedUsers
    sudo groupadd -g 2006 ExternalUsers
    sudo groupadd -g 2007 InternalUsers

    sudo useradd internal_users -g InternalUsers -s /bin/sh
    sudo useradd restricted_user -G RestrictedUsers,ExternalUsers -s /binfalse


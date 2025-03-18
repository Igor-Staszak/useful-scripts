#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: known_hosts <IP>"
  exit 1
fi

ssh-keygen -f "$HOME/.ssh/known_hosts" -R "$1"

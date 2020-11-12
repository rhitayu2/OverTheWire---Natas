#!/bin/bash
address='natas22.natas.labs.overthewire.org/index.php?revelio=true'
authorization='Basic: bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg=='
content=$(curl --user natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ -H "${authorization}" "${address}")
echo "$content"


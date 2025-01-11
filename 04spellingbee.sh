gunzip -c dictionary.gz | grep -v '[^zonicar]' | grep "r" | grep -E '^.{4,}$' | wc
gunzip -c dictionary.gz | grep -v '[^zonicar]' | grep "r" | grep -E '^.{4,}$'
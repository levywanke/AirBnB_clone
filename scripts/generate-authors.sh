#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# Explore ".mailmap" for information on deduplicating email addresses and names.

{
	cat <<-'EOH'
		# The following document enumerates all individuals who have contributed content to the repository.
		# Refer to `hack/generate-authors.sh` for insights into its generation process.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} >AUTHORS


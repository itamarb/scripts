artifactory('hts-itamarb-db-lb'){
   localRepository("docker-local") {
     packageType "docker"
     description "My local Docker registry"
   }
}

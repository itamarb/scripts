artifactory('hts-itamarb-db-lb') {
repoLayouts {
  repoLayout ('test-layout') {
    folderIntegrationRevisionRegExp "SNAPSHOT"
    fileIntegrationRevisionRegExp "SNAPSHOT|(?:(?:[0-9]{8}.[0-9]{6})-(?:[0-9]+))"
    distinctiveDescriptorPathPattern true
    artifactPathPattern "[orgPath]/[module]/[baseRev](-[folderItegRev])/[module]-[baseRev](-[fileItegRev])(-[classifier]).[ext]"
    descriptorPathPattern "[orgPath]/[module]/[baseRev](-[folderItegRev])/[module]-[baseRev](-[fileItegRev])(-[classifier]).pom"
  }
} 
}

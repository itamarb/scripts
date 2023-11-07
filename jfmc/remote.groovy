repoName = userInput (
    type: "STRING",
    value : "maven-remote",
    description : "please provide a repository name"
  )
repoType = userInput (
  type: "STRING",
  value : "Maven",
  description : "please choose a repository type"
  )

userName = userInput (
  type: "STRING",
  value : "admin",
  description : "please enter user name"
  )

password = userInput (
  type: "STRING",
  value : "password",
  description : "please enter password"
  )

artifactory('hts-itamarb-db-lb') {
remoteRepository(repoName) {
  username userName
  password password
  proxy ""
  description "Public description"
  notes "Some internal notes"
  includesPattern "**/*" // default
  excludesPattern "" // default
  packageType repoType // "maven" | "gradle" | "helm" | "ivy" | "sbt" | "nuget" | "gems" | "npm" | "bower" | "debian" | "pypi" | "docker" | "yum" | "vcs" | "p2" | "generic"
  remoteRepoChecksumPolicyType "generate-if-absent" // default | "fail" | "ignore-and-generate" | "pass-thru"
  handleReleases true // default
  handleSnapshots true // default
  maxUniqueSnapshots  0 // default
  suppressPomConsistencyChecks false // default
  offline false // default
  blackedOut false // default
  storeArtifactsLocally true // default
  socketTimeoutMillis 15000
  localAddress "123.123.123.123"
  retrievalCachePeriodSecs 43200 // default
  failedRetrievalCachePeriodSecs 30 // default
  missedRetrievalCachePeriodSecs 7200 // default
  unusedArtifactsCleanupEnabled false // default
  unusedArtifactsCleanupPeriodHours 0 // default
  fetchJarsEagerly false // default
  fetchSourcesEagerly false // default
  shareConfiguration false // default
  synchronizeProperties false // default
  propertySets // (["ps1", "ps2"])
  allowAnyHostAuth false // default
  enableCookieManagement false // default
  xrayIndex false
  blockXrayUnscannedArtifacts false
  xrayMinimumBlockedSeverity "" // "Minor" | "Major" | "Critical"
  enableFileListsIndexing false //default
  blockMismatchingMimeTypes false // default
  bowerRegistryUrl "https://registry.bower.io" //default
  bypassHeadRequests false // default
  clientTlsCertificate "" // default
  composerRegistryUrl "https://packagist.org" // default
  assumedOfflinePeriodSecs 300 // default
  hardFail false // default
  repoLayoutRef // "maven-2-default"
  vcsGitDownloadUrl "" // default
  vcsGitProvider "GITHUB" // default "BITBUCKET" | "OLDSTASH" | "STASH" | "ARTIFACTORY" | "CUSTOM"
  vcsTpe "GIT" // default
}
}

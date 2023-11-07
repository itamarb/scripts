exclude = userInput (
    type: "STRING",
    value : " ",
    description : "please provide an exclude pattern"
  )

artifactory('hts-itamarb-db-lb'){
  localRepository("my-repository") {
  description "Description"
  includesPattern "**/*" // default
  excludesPattern exclude // default
 }
}
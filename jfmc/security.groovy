Instances = userInput (
  type: "ARTIFACTORY",
  multivalued: true,
  description: "All Instances"
  )

userName = userInput (
    type: "STRING",
    value : "itamarb",
    description : "please provide a user name"
  )

groupName = userInput (
    type: "STRING",
    value : "test_group",
    description : "please provide a group name"
  )

artifactory('hts-itamarb-db-lb'){
security {

groups {
    group(groupName) {
      description 'desc_1'
      autoJoin false
    }
  }

  users {
    user(userName) {
      email 'itamarb@jfrog.com'
      password 'password'
      admin false
      profileUpdatable false
      internalPasswordDisabled false
      groups ([groupName]) // values (['groupA', 'groupB']) are examples. Please set existing values from the instance
    }
  }
  
  permissions {
    permission('test_permission') {
      includesPattern '**'
      excludesPattern ''
      anyLocal false
      anyRemote false
      anyDistribution false
      repositories (["libs-release-local", "generic-local"]) // values (["local-rep1", "local-rep2", ...]) are examples. Please set existing values from the instance
      users {
        "$userName" (['manage', 'delete', 'deploy', 'annotate', 'read']) // value userA - is example. Please set existing user names from the instance
      }
      groups {
        "$groupName" (['manage', 'delete', 'deploy', 'annotate', 'read']) // value groupsG1 - is example. Please set existing group names from the instance
      }
    }
  }
} 
}
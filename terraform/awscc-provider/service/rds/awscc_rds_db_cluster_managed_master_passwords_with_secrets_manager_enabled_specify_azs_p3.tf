# Write Terraform configuration that creates RDS db cluster with managed master password with secrets manager enabled, use awscc provider

resource "awscc_rds_db_cluster" "example_db_cluster" {
  availability_zones          = ["us-east-1b", "us-east-1c"]
  engine                      = "aurora-mysql"
  db_cluster_identifier       = "example-dbcluster"
  manage_master_user_password = true
  master_username             = "foo"
}

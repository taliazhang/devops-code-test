resource "local_file" "count_int_loop" {
  count = var.number
  content = "This is file number ${count.index}"
  filename = "${path.module}/${count.index}.txt"
}
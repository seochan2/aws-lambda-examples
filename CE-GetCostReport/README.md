Get Cost and Usage Report
=============

### Create the lambda function

* Runtime : Python 3.7

### Creating IAM permissions

Create a Policy :

* IAM > Policies > Create policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ce:GetCostAndUsage",
            "Resource": "*"
        }
    ]
}
```
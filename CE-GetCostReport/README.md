Get Cost and Usage Report
=============

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
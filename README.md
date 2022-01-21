# Python CRUD within SQL Server

## Install the Microsoft ODBC driver for SQL Server (macOS)

Install the ODBC driver via brew:

```brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release && brew update && HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools```

## Deploy SQL Server localy

Start a mssql-server instance using the latest update for SQL Server 2017:

```docker run --name mssql-server -e "HOMEBREW_NO_ENV_FILTERING=1" -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=P@ssw0rd123" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest```

You can connect to the SQL Server using the sqlcmd tool inside of the container by using the following command on the host:

```docker exec -it mssql-server /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd123```

## Create a new database

```sqlcmd -S localhost -U sa -P P@ssw0rd123 -Q "CREATE DATABASE EmployeesDB;"```

## Create a new table

```sqlcmd -S localhost -U sa -P P@ssw0rd123 -d EmployeesDB -Q "CREATE TABLE Employees (Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY, Name NVARCHAR(50), Location NVARCHAR(50));"```

## Insert some data

```sqlcmd -S localhost -U sa -P P@ssw0rd123 -d EmployeesDB -Q "INSERT INTO Employees (Name, Location) VALUES (N'Jared', N'Australia'), (N'Nikita', N'India'), (N'Tom', N'Germany');"```

## Run crud.py

You can test the local ODBC connection using the following command on the host:

```pyton3 api.py```
commit
